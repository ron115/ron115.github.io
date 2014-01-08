:: if need to delete the output directory before updating, add a "-d" argument

pelican article-src-en -o ../blog/en -s scripts/pelicanconf_en.py %1
pelican article-src-zh -o ../blog/zh -s scripts/pelicanconf_zh.py %1
