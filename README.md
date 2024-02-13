# PandanSheet(Korean.ver)

`PandanSheet`는 Python에서 Google Sheets를 효율적으로 사용하기 위한 패키지입니다. 이 패키지는 Google Sheets와의 상호작용을 위한 간편한 인터페이스를 제공하여, Google Sheets 문서의 데이터를 pandas DataFrame으로 쉽게 변환하고, 반대로 pandas DataFrame의 데이터를 Google Sheets에 업로드할 수 있게 해줍니다. 또한, 시트 내용의 삭제, 새로운 시트 추가, 지정된 시트의 삭제 등의 기능을 지원합니다.

## 주요 기능

- Google Sheets 문서로부터 데이터를 읽어 pandas DataFrame으로 변환
- pandas DataFrame의 데이터를 Google Sheets에 업로드
- 지정된 시트의 내용 삭제
- 새로운 시트 추가
- 지정된 시트 삭제

## 설치

`PandanSheet` 패키지는 pip를 통해 쉽게 설치할 수 있습니다.

```bash
pip install pandansheet
```
## 사용방법
```py
from pandansheet import Sheet

# Google Sheets 문서의 URL을 사용하여 Sheet 객체 생성
sheet = Sheet(URL="여기에 Google Sheets 문서의 URL 입력")
# Google Sheets 문서의 데이터를 DataFrame으로 변환
df = sheet.to_DataFrame()
print(df)
# 지정된 시트의 내용 삭제
sheet.clear(sheet_name="시트명")
# 새로운 시트 추가
sheet.add(sheet_name="새 시트명")
# 지정된 시트 삭제
sheet.delete(sheet_name="삭제할 시트명")
# DataFrame 데이터를 Google Sheets에 업로드
sheet.to_Sheet(df=df, sheet_name="업로드할 시트명")
```
## 추가 정보
- PandanSheet 패키지를 사용하기 위해서는 Google Apps Script를 통해 생성된 웹 앱의 URL이 필요합니다. 이 웹 앱은 pandansheet 패키지의 기능을 지원하기 위해 Google Sheets API와 상호작용합니다.
- Google Apps Script 웹 앱의 설정 및 배포 방법에 대한 자세한 정보는 Google Apps Script 공식 문서를 참조하세요.
## 라이선스
이 프로젝트는 MIT 라이선스 하에 제공됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.
```bash
위 내용을 `README.md` 파일로 저장하여 사용하세요. 이 파일은 `pandansheet` 패키지의 GitHub 저장소 또는 다른 코드 공유 플랫폼에 추가될 수 있으며, 사용자가 패키지의 기능과 사용 방법을 쉽게 이해할 수 있도록 도와줍니다.
```
# PandanSheet(English.ver)

`PandanSheet` is a package designed for efficient interaction with Google Sheets in Python. It provides a straightforward interface for interacting with Google Sheets, enabling easy conversion of Google Sheets document data into pandas DataFrames and vice versa. This package supports uploading data from pandas DataFrames to Google Sheets, as well as deleting content from specified sheets, adding new sheets, and deleting specified sheets.

## Key Features

- Convert data from Google Sheets documents into pandas DataFrames.
- Upload data from pandas DataFrames to Google Sheets.
- Delete content from specified sheets.
- Add new sheets to the document.
- Delete specified sheets from the document.

## Installation

The `PandanSheet` package can be easily installed using pip.

```bash
pip install pandansheet
```
## How to Use
```py
from pandansheet import Sheet

# Create a Sheet object using the URL of the Google Sheets document
sheet = Sheet(URL="Enter the URL of your Google Sheets document here")
# Convert the data from the Google Sheets document into a DataFrame
df = sheet.to_DataFrame()
print(df)
# Delete the content of a specified sheet
sheet.clear(sheet_name="SheetName")
# Add a new sheet
sheet.add(sheet_name="NewSheetName")
# Delete a specified sheet
sheet.delete(sheet_name="SheetNameToDelete")
# Upload DataFrame data to Google Sheets
sheet.to_Sheet(df=df, sheet_name="SheetNameForUpload")
```
## Additional Information
- To use the PandanSheet package, you will need the URL of a web app created through Google Apps Script. This web app interacts with the Google Sheets API to support the functionalities of the pandansheet package.
- For detailed information on setting up and deploying your Google Apps Script web app, please refer to the official Google Apps Script documentation.
## License
This project is provided under the MIT License. For more details, please refer to the LICENSE file.
```bash
Save the above content as a `README.md` file for use. This file can be added to the `pandansheet` package's GitHub repository or any other code-sharing platform, helping users to easily understand the functionalities and usage of the package.
```