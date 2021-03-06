# ๐ Git

[Git์ด๋?](#%EF%B8%8F-git์ด๋)

[Git Bash๋ฅผ ํ์ฉํ๊ธฐ ์ํ ๊ธฐ๋ณธ ๊ฐ๋](#%EF%B8%8F-git-bash๋ฅผ-ํ์ฉํ๊ธฐ-์ํ-๊ธฐ๋ณธ-๊ฐ๋)

[Git ๊ธฐ์ด ํ๋ฆ](#%EF%B8%8F-git-๊ธฐ์ด-ํ๋ฆ)

[๋ฒ์  ๊ธฐ๋กํ๊ธฐ](#-๋ฒ์ -๊ธฐ๋กํ๊ธฐ)

[Git ๊ธฐ์ด ๋ช๋ น์ด](#-git-๊ธฐ์ด-๋ช๋ น์ด)





## โ๏ธ Git์ด๋?

> Git์ ๋ถ์ฐ ๋ฒ์ ๊ด๋ฆฌ ์์คํ
>
> ๋ฒ์ ๊ด๋ฆฌ?  โ  ๋ฒ์ : ์ปดํจํฐ software์ ํน์  ์ํ



## โ๏ธ Git Bash๋ฅผ ํ์ฉํ๊ธฐ ์ํ ๊ธฐ๋ณธ ๊ฐ๋

> CLI : Command Line Interface (๋ช๋ น์ด๋ก์จ ์ค๋ก ์กฐ์)
>
> ์ปดํจํฐ์ ๋ช๋ น์ ํ๋ ๊ฒ



### ๐ CLI ๋ช๋ น์ด

> $ : Bash์์ ๋ช๋ น์ด ์ฐ๋ ๊ณณ

- **pwd** (print working directory) : ํ์ฌ directory ์ถ๋ ฅ 				โ  directory = ํด๋/ํ์ผ
- **cd** (change directory) : ๋๋ ํ ๋ฆฌ ์ด๋                                         โ  cd .. = ๋ค๋ก๊ฐ๊ธฐ
- **ls** (list) : ๋ชฉ๋ก
- **mkdir** (make directory) : ํด๋ ์์ฑ
- **touch** : ํ์ผ ์์ฑ
- **/** : ๋ฐ์ด ์ฐ๊ธฐ ๊ณต๋ฐฑ
- **rm** (remove) : ํ์ผ ์ง์ฐ๊ธฐ / **rm -r ํด๋์ด๋ฆ** : ํด๋ ์ง์ฐ๊ธฐ





## โ๏ธ Git ๊ธฐ์ด ํ๋ฆ

> ์ปดํจํฐ ํ์ผ์ ๋ณ๊ฒฝ์ฌํญ์ ์ถ์ ํ๊ณ  ์ฌ๋ฌ ๋ช์ ์ฌ์ฉ์๋ค ๊ฐ์ ํด๋น ์์์ ์กฐ์จํ  ์ ์๋ค

![process](Git.assets/process.png)

- **Working Directory** : ์์(์์ )ํ ํ์ผ
- **Staging  Area** : ๋ฒ์ ์ผ๋ก ๊ธฐ๋กํ  ํ์ผ์ ๋ชจ์ผ๋ '์์๊ณต๊ฐ'
- **Repository** : ๋ฒ์ ๋ค์ด ๊ธฐ๋ก๋๋ ๊ณณ



### ๐ ๋ฒ์  ๊ธฐ๋กํ๊ธฐ

1. **$ git init**

   ```bash
   # git init์ ์๋ ฅํ๋ฉด, ์ดํ์ (master)๊ฐ ํ๊ธฐ๋จ
   # ๊ทธ๋ฌ๋ฉด .git ํด๋๊ฐ ์์ฑ๋ ๊ฒ
   ADMIN@LAPTOP-M3AAIA8I MINGW64 ~/OneDrive/Desktop/TIL (master)
   $ git init
   Reinitialized existing Git repository in C:/Users/ADMIN/OneDrive/Desktop/TIL/.git/
   ```

โ	๐จ *๋ง์ฝ (master)๊ฐ ์์ฑ์ด ์ ๋  ๊ฒฝ์ฐ*     ์๋ ๋ด์ฉ ์ถ๊ฐ

โ	`$ git config --global user.name 'Github username'`

โ	`$ git config --global user.email 'Github email'`

โ	๐จ ํ์ธ์ ํ  ๋๋

โ	`$ git config --global --list`



2. **$ git status** (๋ณ๊ฒฝ๋ ๊ฒ์ด ์๋์ง ํ์ธ์ด ๊ฐ๋ฅ)

   ```bash
   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   markdown/Git.md
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           markdown/Git.assets/
   
   no changes added to commit (use "git add" and/or "git commit -a")
   
   # ์ฌ๊ธฐ์ modified (์์ ), untracked file (์๋ก ๋ฐ๊ฒฌ๋ ํ์ผ)์ด ๋นจ๊ฐ์์ผ๋ก ๊ธฐ๋ก๋๋ค
   # ์์ ๋, ์๋ก์ด ํ์ผ๋ค์ ํ์ฌ Working directory์ ์์ง๋ง, 'git add'๋ฅผ ํตํด Staging Area๋ก ๋ณด๋ธ๋ค
   ```

   

3. **$ git add ํ์ผ ์ด๋ฆ / $ git add . (์ ์ฒด ๋ค ์์  ํ  ๋์)**

   ```bash
   ADMIN@LAPTOP-M3AAIA8I MINGW64 ~/OneDrive/Desktop/TIL (master)
   $ git add .
   
   # ํ์ฌ ์์  ๋๋ ์๋ก์ด ํ์ผ์ Working directory์์ Staging Area(์์๊ณต๊ฐ)์ ์ฎ๊ฒจ์ก๋ค
   
   ADMIN@LAPTOP-M3AAIA8I MINGW64 ~/OneDrive/Desktop/TIL (master)
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
   # staged๋ผ๋ ๊ฒ์ ์ปค๋ฐํ๊ธฐ ์  ์คํ์ด์ง์ ์๋ค๋ ๊ฒ (staging area์ ํ์ผ์ด ์๋ค๋ ๊ฒ)
                       
           new file:   "markdown/Git.assets/\355\231\224\353\251\264 \354\272\241\354\262\230 2022-07-05 171325.png"
           modified:   markdown/Git.md
           
   # git add๋ฅผ ์๋ ฅ ํ git status๋ฅผ ์ฐ๋ฉด ๋นจ๊ฐ์์์ ์ด๋ก์์ผ๋ก ๋น ๊ท๋ค
   # new file + modified ์ด๋ก์์ผ๋ก ๋ณด์ธ๋ค
   ```

   

4. **$ git commit -m '์ปค๋ฐ ๋ฉ์์ง'**

   ```bash
   #์ปค๋ฐ์ ํตํด ๋ฒ์ ์ผ๋ก ๊ธฐ๋ก
   
   $ git commit -m 'TIL ์๋ฐ์ดํธ 3'
   [master 87e9989] TIL ์๋ฐ์ดํธ 3
    2 files changed, 90 insertions(+)
    create mode 100644 "markdown/Git.assets/\355\231\224\353\251\264 \354\272\241\354\262\230 2022-07-05 171325.png"
   ```

   

5. **$ git log**

   ```bash
   #git log๋ฅผ ํตํด ํ์ฌ ์ ์ฅ์์ ๊ธฐ๋ก๋ ์ปค๋ฐ์ ์กฐํํ  ์ ์๋ค
   
   $ git log
   commit 87e9989e27ca5de4018fe90c36b65323a592451c (HEAD -> master)
   Author: JeJoonLee <jejoonlee1996@gmail.com>
   Date:   Tue Jul 5 17:41:59 2022 +0900
   
       TIL ์๋ฐ์ดํธ 3 #์กฐํ๋ ์ปค๋ฐ ๋ฉ์ธ์ง
   
   commit 89a758d7767d5fc57811f750c36053e5f786d279
   Author: JeJoonLee <jejoonlee1996@gmail.com>
   Date:   Tue Jul 5 17:05:48 2022 +0900
   
       TIL ์๋ฐ์ดํธ 2
   
   commit 28555b0d36a1c6d9e52c67bfe9716f4f23b54c2d
   Author: JeJoonLee <jejoonlee1996@gmail.com>
   Date:   Tue Jul 5 16:56:33 2022 +0900
   
       TIL ์๋ฐ์ดํธ
   ```

   **$ git log -1** : ์ต๊ทผ ํ๊ฐ์ ์ปค๋ฐ

   **$ git log  --oneline** : ์ปค๋ฐ์ ํ์ค๋ก

   **$ git log -2 --oneline** : ์ต๊ทผ 2๊ฐ ์ปค๋ฐ์ ํ์ค๋ก



### ๐ Git ๊ธฐ์ด ๋ช๋ น์ด

| ๋ช๋ น์ด                       | ๋ด์ฉ                                                         |
| :--------------------------- | :----------------------------------------------------------- |
| git init                     | ๋ก์ปฌ ์ ์ฅ์ ์์ฑ (์ดํ ํ์ผ ์ด๋ฆ ์์ master๋ผ๊ณ  ๋ธ)         |
| git add <ํ์ผ๋ช>             | ํน์  ํ์ผ/ ํด๋์ ๋ณ๊ฒฝ์ฌํญ ์ถ๊ฐ                              |
| git commit -m '<์ปค๋ฐ๋ฉ์ธ์ง>' | ์ปค๋ฐ (๋ฒ์  ๊ธฐ๋ก)                                             |
| git status                   | ์ํ ํ์ธ (modified, untracked, staged๋ก ํ์ผ์ ํ ์ํ๋ฅผ ํ์ธ) |
| git log                      | ๋ฒ์ ํ์ธ                                                     |





