# Git flow 관련

1. feature 브랜치를 develop에서 분기하기

   `git checkout -b feature/<name> develop` 

2. feature 브랜치에서 develop으로 이동하기

   `git checkout develop`

3. feature 브랜치에서 변경한 내용을 develop에 병합하기

   `git merge --no--ff feature/<name>`

4. 병합하고 난 후 feature 브랜치를 삭제하기

   `git branch -d feature/<name>`

5.  develop 브랜치를 원격 중앙 저장소에 올린다

   `git push origin develop`







