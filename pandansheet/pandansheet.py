import pandas as pd
import requests

class Sheet:
    #googlesheet의 기본적은 기능(새시트 추가, 시트내용 삭제)이 들어간 URL
    __URL='https://script.google.com/macros/s/AKfycbwW5mrJ6zAaDq7yFkjILhb-AoJcOuSU-E2_ui_mN0mzCRtkMjgz2NVZrls862ofkhiw-g/exec'
    #기본 생성자 해당 URL에 있는 시트를 바탕으로 DataFrame을 만듦
    def __init__(self,URL:str, type='xlsx', gid=None, cell_range=None, encoding='utf-8'):
        data=URL.split('/')
        index=data.index('d')+1
        self.__id=data[index]
        URL=f'https://docs.google.com/spreadsheets/d/{self.__id}/export?format={type}'
        if gid is not None:
            URL += f'&gid={gid}'
        if cell_range is not None:
            URL += f'&range={cell_range}'   
        if type == "tsv":
            self.__df= pd.read_csv(URL, sep='\t', encoding=encoding)
        elif type == "csv":
            self.__df= pd.read_csv(URL, encoding=encoding)
        elif type == "xlsx":
            self.__df= pd.read_excel(URL)
        else:
            raise TypeError('확장자(type)를 tsv, csv, xlsx으로 설정해주세요.(type is Only tsv, csv, and xlsx are available.)')
    #DataFrame을 반환함
    def to_DataFrame(self):
        return self.__df
    #해당 URL의 다른 시트내용을 지움
    def clear(self, sheet_name:str):
        www = requests.post(url=self.__URL, data={'id': self.__id, 'name': sheet_name,'action':'clear'})
        if www.status_code != 200:
            raise ValueError("시트내용을 못지웠습니다.(Failed to clear the sheet.)")
    #해당 URL의 다른 시트를 지움
    def delete(self, sheet_name:str):
        www = requests.post(url=self.__URL, data={'id': self.__id, 'name': sheet_name,'action':'delete'})
        if www.status_code != 200:
            raise ValueError("시트내용을 못지웠습니다.(Failed to clear the sheet.)")
    #해당 URL의 새로운 시트를 추가함
    def add(self, sheet_name:str):
        www = requests.post(url=self.__URL, data={'id': self.__id, 'name': sheet_name,'action':'add'})
        if www.status_code != 200:
            raise ValueError("새 시트를 추가하지 못했습니다.(Failed to add the sheet.)")
    #해당 sheet에 반환함
    def to_Sheet(self, df:pd.DataFrame, URL:str, sheet_name:str, parameter:list=None, columns:bool=True):
        self.clear(sheet_name)
        if parameter is None:
            parameter = df.columns.tolist()
        if len(parameter) != len(df.columns):
            raise ValueError("파라미터와 칼럼의 개수가 일치하지 않습니다.")
        if columns:
            col_data = {key:value for key,value in zip(parameter, df.columns)}
            response = requests.post(url=URL, data={'operation': 'upload', 'data': col_data})
            if response.status_code != 200:
                raise ValueError(f"컬럼 이름 전송 실패(fail)\ndata : {col_data}")
        for index, row in df.iterrows():
            data = {key:row[value] for key,value in zip(parameter, df.columns)}
            response = requests.post(url=URL, data={'operation': 'upload', 'data': data})
            if response.status_code != 200:
                raise ValueError(f"데이터 전송 실패(fail)\ndata : {data}")
