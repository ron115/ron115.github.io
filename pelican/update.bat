:: if need to delete the output directory before updating, add a "-d" argument

pelican article-src-en -o ../article/en -s scripts/pelicanconf_en.py %1
pelican article-src-zh -o ../article/zh -s scripts/pelicanconf_zh.py %1
