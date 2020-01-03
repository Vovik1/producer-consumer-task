# producer-consumer-task
Завдання/Task
На підприємстві є робот. Є N задач, які потрібно робити роботу одна за одною у строго визначеному порядку, починаючи із певної заданої задачі. Коли всі ці задачі над поточним об'єктом зроблені - роботу потрібно повторити цикл задач, тільки над іншим об'єктом.
Роботу потрібно подавати задачі одна за одною з мінімальною затримкою.
Оператор може дописати нову задачу до чи після якоїсь задачі без зупинки виробництва.  Ця нова задача буде виконуватися роботом або над поточним об'єктом, або вже над наступним. До того ж, якщо оператор дописав задачу перед стартовою - то тепер з цієї задачі робот буде починати після його перезавантаження.
Задачі мають назву та містять також певні стрічкові пояснення для робота.
Написати API отримання задач для робота та налаштування задач для оператора, написати імплементацію на мові python. Написати документацію для оператора. Вважати, що функціонал збереження даних оператора на диск та CLI для оператора писатиме хтось інший.

The company has a robot. There are N tasks that need to be done one by one in a strictly defined order, starting with a specific task. When all these tasks over the current object are done, the robot should repeat the tasks cycle, but with the new object. The task should be submitted one by one with minimum delay.
An operator can add a new task before or after any task without stopping production. This new task will be performed either on the current object or on the next object. In addition, if the operator completed the task before the start - new cycle will run starting with this task.
The tasks are named and also contain some string explanations for the robot.
Write an API for getting tasks for the robot and setting up tasks for the operator, write implementation in python. Write documentation for the operator. 

Пояснення до виконання/Explanations
Для імітації праці робота необхідно запустити програму reciever.py. Після запуску на екрані появлятимуться послідовно задачі, які виконує робот. Задачі для робота підготовлені зазделегіть. Для того, щоб додати задачу для виконання роботом необхідно запустити програму sender.py. Після запуску програми на екрані появиться стрічка для вводу команди. Команда для робота має наступний шаблон: ">>Назва_інструкції Стрічкове_пояснення_для_робота 1", де 1 вказує місце в списку задач. У разі неправильного введення команди робот продовжить свою роботу.Для зупинки робота оператор повинен надіслати команду "break". 

To simulate a robot work, you must run reciever.py. Upon startup the program, the tasks that the robot performs will appear on the screen. Tasks for the robot prepared in advance. To add a task for robot run sender.py. After starting the program, a command entry bar appears on the screen. The command for the robot has the following template: ">> Instruction_name Tape_explanation_for_robot 1", where 1 specifies a place in the task list. If the command is incorrectly entered, the robot will continue its work. To stop a robot an operator has to send "break" message.
