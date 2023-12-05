# introduction
git init
python -m venv ./env
source env/bin/activate
conda deactivate
pip install -r requirements.txt
deactivate

개발하다 보면 import를 하고 난 후 사용하지 않는 경우가 있다. 이러한 경우 일일이 지워주어야 하는데 이것 또한 귀찮은 일이다. 이것을 간단하게 해결하는 방법이 있다.
[mac 기준] 명령어 : command + shift + p 한 후 Organize Imports 선택
출처: https://codiving.kr/99 [코드에 빠지다:티스토리]