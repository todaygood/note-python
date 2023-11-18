

.ipynb: “.ipynb” 文件是使用 Jupyter Notebook 来编写Python程序时的文件。Jupyter Notebook（此前被称为 IPython notebook）是一个交互式笔记本，支持运行 40 多种编程语言。在jupyter下的File—>Download as —>python(.py)可以将.ipynb转化为.py文件。


Jupyter notebook简洁易用，已成为数据分析、机器学习领域的宠儿。如果大家在运行程序的过程中，出现了bug，免不了需要进行调试。在IDE（集成开发环境）中调试和在Jupyter notebook中调试还是有区别的。今天我们来学习下如何在Jupyter notebook中调试程序。

使用import pdb 的方式进行调试python ,参见https://aiwithcloud.com/2021/11/28/%e5%9c%a8jupyter-notebook%e4%b8%ad%e8%b0%83%e8%af%95python%e7%a8%8b%e5%ba%8f/

好痛苦， 程序是调试出来的，不是写出来的，因此在PyCharm中调试程序，会香很多. 


Jupyter notebook 适合啥？ 适合学习一个新的Python库时写笔记， 一边写Python单句程序，一边写笔记用的。 


参见 Anaconda介绍、安装及使用教程  https://zhuanlan.zhihu.com/p/32925500


2. 切换环境

① Linux 或 macOS

source activate <env_name>


② Windows

activate <env_name>


4. 显示已创建环境

conda info --envs
或

conda info -e
或

conda env list





