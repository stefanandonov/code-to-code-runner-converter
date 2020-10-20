## Python скрипта за конвертирање на задачи од code.finki.ukim.mk во CodeRunner квиз прашања

##### Изработено од: Стефан Андонов

Напомена: Моментално го поддржува само програмскиот јазик C и не работи со скриени тест примери. 

### Упатство за користење

1. Креирајте директориум во којшто ќе ги зачувате .json фајловите за задачите од code. Директориумот треба да ја има следната хиерархија: (Категорија може да се однесува пример на лабораториска вежба 1, 2, 3 итн.)

    ---root \
    ------kategorija1 \
    ---------zadaca1.json \
    ---------zadaca2.json \
    ---------zadaca3.json \
    ... \
    ---------zadacaN.json \
    ------kategorija2 \
    ---------zadaca1.json \
    ---------zadaca2.json \
    ---------zadaca3.json \
    ... \
    ---------zadacaN.json \\
    ... \
    ------kategorijaN \
    ---------zadaca1.json \
    ---------zadaca2.json \
    ---------zadaca3.json \
    ... \
    ---------zadacaN.json \\
    
    
2. Преземете ги задачите во json формат (една по една) од code.finki.ukim.mk, со десен клик на Export, Save Link As и зачувајте го секој .json фајл во соодветниот директориум согласно категоријата на која што сакате да припаѓа задачата.

3. Клонирајте го овој репозиториум со наредбата `git clone https://github.com/stefanandonov/code-to-code-runner-converter.git`. Влезете во директорумот со `cd code-to-code-runner-converter`

4. Инсталирајте ги потребните библиотеки со помош на `pip3 install -r requirements.txt`. Секако, прво влезете преку терминал во соодветниот директориум.

5. Извршете преку терминал `python3 code_to_code_runner_converter.py -i <input_folder_path> -o <output_folder_path>`. Пример: `python3 code_to_code_runner_converter.py -i /Users/stefanandonov/Documents/SP_labs -o /Users/stefanandonov/Documents/SP_labs/xml_files`

6. Во output фолдерот ќе ви се изгенерираат xml фајлови (по еден за секоја категорија). Отворете courses.finki.ukim.mk (или ispiti.finki.ukim.mk). Потоа отворете Question Bank, па Import. Како формат за import одберете Moodle XML. Прикачете ги еден по еден изгенерираните xml фајлови и импортирајте. Напомена: Пред импортирање отворете ги фајловите во некое IDE и проверете дали има грешки (некој специјален карактер може би ќе треба рачно да го смените).
