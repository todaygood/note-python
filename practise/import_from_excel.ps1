

$proj_path = "C:\Users\HuJun\Documents\My-Github\eagleeye\"
$python_env=$proj_path+"venv\scripts\activate.ps1"
Invoke-Expression -Command $python_env


python $proj_path\utils\batch_add_stocks_from_excel.py  $args[0]