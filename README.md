# -tf_idf-
用统计方法tf_idf来实现资讯的关键词抽取

1.数据准备

     停用词文件（给出）
     
     新闻语料(txt文件)--放在一个文件夹下(可去：http://www.sogou.com/labs/resource/ca.php 下载)
     
2.逻辑架构

     a.对新闻语料进行清洗-分词-去停用词-去标点符号等
     
     b.构建每篇文章的字典
     
     c.计算所有词的tf_idf
     
     d.将每篇文章的tf_idf写入新的文件夹
