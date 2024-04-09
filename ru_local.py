MOVE_1 = 'Ход первой команды'
MOVE_2 = 'Ход второй команды'
MOVE_3 = 'Ход третьей команды'
REMOVAL = 'Как быстро летит время. Кажется, что всё было ещё впереди. Вы проиграли.'
STOCK = ['Деньги', 'Земля', 'Ресурсы', 'Люди', 'Оружие']
CHOICE = '''За кого вы хотите играть:
1) Вашингтонский освободительный фронт
2) "Цикада"
3) Община
Ваш ответ: 1/2/3'''
INTRODUCTION_1 = '''Очнитесь, солдаты! После смерти своего лидера Вашингтонский освободительный фронт, как никогда, 
оказался на грани распада. Попробуйте сохранить и преумножить оставшиеся ресурсы и найти возможность отомстить своим 
врагам!
'''
INTRODUCTION_2 = '''После прошлого нападения на ваш штаб был убит единственный человек, способный изготовить вакцину
против заражения. "Цикады" распались. Но вы ещё не достигли своих целей. Недавно вашу реорганизованную группу посетили
беженцы с Сиэтла с новостями о перспективах роста. Этот шанс вы так просто не упустите.
'''
INTRODUCTION_3 = '''Устав от гнёта контрадандистов и заражённых, вы преобразовали своё поселение в защищённую крепость.
Вашей задачей является сохранить свой стабильный рост и не нажить врагов.
'''
EVENT_1_0 = '''Никаких новостей. Штиль на фоне разворачивающихся событий ощущается умиротворяюще спокойно.
'''
EVENT_1_1 = '''Значительная часть Сиэтла была заброшена и со временем её окупировали заражённые. Вы можете расширить
часть своей территории, направив туда группу из 10 человек. Ваш ответ: да/нет
 '''
EVENT_1_1_YES = '''Не все люди, направленные на чистку территорий от заражённых, вернулись. Однако задачу, которую вы
ставили перед ними, они выполнили полностью. Ваша территория увеличена: +100 земли, -5 людей
'''
EVENT_1_1_NO = '''Вы выбрали не рисковать жизнью своих людей и решили отложить экспансию на потом.
'''
EVENT_1_2 = '''Вы находите чертежи оружия, словно нарочно оставленные кем-то. Попробуете ли вы создать его и экипировать
ваших солдат? Ваш ответ: да/нет
'''
EVENT_1_2_YES = ('Вы решили увеличить количество своих боеприпасов. Получен доступ к новому оружию: -10 ресурсов,'
                 ' +20 оружия')
EVENT_1_2_NO = '''Вы решили сберечь свои ограниченные запасы и психологическое здоровье своих людей. Всё ведь будет
хорошо, верно?
'''
EVENT_1_3 = '''Вы слышали о повторном объединении "Цикад". Почему бы вновь не начать сотрудничество? Ваш ответ: да/нет
'''
EVENT_1_3_YES = '''"Цикады" приняли ваше предложение. Теперь вы союзники. И хоть сейчас нет видимых преимуществ - будущее
всё покажет.
'''
EVENT_1_3_NO = '''Те, кто помнил о благих целях "Цикад" по поиску вакцины, услышав новость о их возвращении
предпочли оставить ВОФ и перебрались к ним: -20 людей'''
CITIZENS_COMPLAINTS = '''Выжившие, которых вы приняли в качестве бесплатной рабочей силы в обмен на защиту, не знают
к кому обратиться со своими проблемами. Чтобы предотвратить разбой, вы решили пригласить особо недовольных. Кому из них
вы поможете сегодня? Ваш ответ: да/нет 
'''
EVENT_1_4 ='''Напасть на вторую команду'''
EVENT_1_4_YES = '''Нападение прошло успешно. У противника -50 людей, -100 оружия'''
EVENT_1_4_NO = '''Вы решили не рисковать'''
HELP = 'Помочь'
CITIZENS_1 = ['Томасу: ', 'Эмили: ', 'Меттью: ', 'Валентину: ']
COMPLAINTS = ['10 запасов', '5 запасов', '20 запасов', '20 денег']
EVENT_2_1 = '''На острове, где расположилась ваша база нет никого, кроме вас и заражённых. Именно поэтому плохая погода
застаёт вас в расплох: -20 ресурсов и -10 оружия. Если вы ничего не сделаете, то потеряете ещё больше.
Укрепляем склад? Ваш ответ: да/нет
'''
EVENT_2_1_YES = ('Без сомнения, ваше решение было разумным. Вы решили понести небольшие потери сейчас, чтобы избежать '
                 'их в будущем: -10 ресурсов')
EVENT_2_1_NO = '''Вы решили сэкономить имеющиеся ресурсы на обустройстве склада, однако это не было рационально. В этот
раз вы обошлись небольшими потерями: -25 ресурсов, -4 оружия
'''
EVENT_2_2 = '''Ваше долгое отсутствие в информационном поле перечеркнуло лояльность многих людей, разделявших с вами
убеждения. Как на счёт того, чтобы приобрести собственную радиоволну для расширения диапазона влияния, как в старые
добрые? Ваш ответ: да/нет
'''
EVENT_2_2_FIRST_YES = '''К сожалению, нанятый контрабандист обманул вас, продав не работающую технику: -30 денег
'''
EVENT_2_2_SECOND_YES = '''Поздравляю, вы можете начинать радиовещание: -30 денег
'''
EVENT_2_2_NO = '''Вы решили отложить идею в дальний ящик. Есть куда более важные дела.
'''
EVENT_2_3 = '''Вы налаживаете торговые отношения с переменно посещающими остров контрабандистами. Однако партнёрство не
позволяет вам ослабить бдительность, поэтому вы приставляете к ним патруль, провожающий до причала. Доверяете ли вы
чутью и приставите отряд к торговцам? Ваш ответ: да/нет
'''
EVENT_2_3_FIRST_YES = '''Увы, по дороге на причал ничего не произошло. Однако недостаток вооружённых людей на разведке 
способствовал удачному нападению со стороны заражённых. Вы потеряли часть своих лучших разведчиков: - 20 людей
'''
EVENT_2_3_SECOND_YES = '''А вы случайно не экстрасенс? Ваши люди заметили, что часть погруженного продовольствия на
лодке контрадандистов, принадлежит "Цикаде". В результате перестрелки вы получили назад запасы и деньги в качестве 
компенсации: +40 ресурсов, +60 денег
'''
EVENT_2_3_NO = '''Вы не считаете важным проверять надёжность ваших партнёров. Недосчёт части провианта и сырья ничем
не обоснован: -20 ресурсов
'''
EVENT_2_0 = '''Никаких новостей. Шелест листвы напоминает вам о далёких временах. Кажется, на горизонте можно увидеть
приближающееся судно.
'''
AUCTION = '''Выбор острова в качестве вашего основного местоположения был неслучайным. Тишина, отсутствие незванных 
гостей и огромные просторы для роста. Вы не ожидали, что до вас здесь обитали какие-то люди, поэтому найденные журналы
с модификациями приводят в восторг и вас, и торговцев. Вам осталось лишь решить: что вы им продадите? Ваш ответ: 
количество продукции
1) Изготовление дымовых снарядов - оценивается в 13 денег
2) Улучшение глушителей - оценивается в 40 денег
3) Изготовление разрывных стрел - оценивается в 13 денег
4) Улучшение мины ловушки - оценивается в 50 денег
5) Изготовление зажигательных патронов - оценивается в 29 денег
'''
AUCTION_1 = ['Дымовух: ', 'Глушителей: ', 'Стрел: ', 'Ловушек: ', 'Патронов: ']
EVENT_3_0 = '''Солнце играет бликами на возвышающихся форпостах. Воздвигнутые вами стены кажутся безопасными. Сегодня
ничего не происходит. Можно выдохнуть.
'''
EVENT_3_1 = '''Несколько человек из населения общины выдвинули идею о воздвижении церкви для причащения. Вы размышляете
насколько данная идея стоит трату ограниченных запасов и людских сил. Ваш ответ: да/нет
'''
EVENT_3_1_FIRST_YES = '''Строительство церкви сыграло вам на руку. Внедрив несколько приближенных человек в епархию, вы
получили сведения о настроениях, ходящих среди населения: -50 ресурсов
'''
EVENT_3_1_SECOND_YES = '''Рабочие, отправленные на строительство церкви, оказались недостающими на пограничных постах.
Из-за этого поставленные несколько добровольцев на их место погибли в сражении с заражёнными: -50 ресурсов, -20 людей 
'''
EVENT_3_1_FIRST_NO = '''Несколько особо религиозных человек устроили забастовку на площади. Они отказались подчиняться и
мирно урегулировать возникшие проблемы. Вам пришлось применить грубую силу, что привело к жертвам: -50 ресурсов.
'''
EVENT_3_1_SECOND_NO = '''Жители общины смирились с отсутствием церкви, они направили свои мысли в более злободневные 
дела. Кто-то предпочёл углубиться в анимализм. Теперь в районе главной площади возвышается грубо выстроганный из дерева
тотем.
'''
EVENT_3_2 = '''Вы слышали, что "Цикады" вернулись и наращивают влияние. Их популярность среди жителей общины возрастает.
Скорее всего, кто-то намеренно распостраняет слухи и агитирует людей присоединиться к собирающейся группировке.
Хотите ли вы проверить наличие пропагандиста в ваших рядах? Ваш ответ: да/нет
'''
EVENT_3_2_FIRST_YES = '''Волноваться было не о чем. Наводка на агитатора оказалась ложной. Вы впустую потратили
деньги на покупку информации: -50 денег
'''
EVENT_3_2_SECOND_YES = '''Полученная наводка стоила потраченных денег. Ваша интуиция не подвела, население прислушалось
к вам и осталось, услышав об опасном пути и ненадёжности информатора: -50 денег, -3 человека'''
EVENT_3_2_NO = '''Вы полагаете, что у каждого есть собственное право выбора, поэтому просто закрываете глаза на 
постоянный отток населения. Люди пользуются вашим безразличием, забирают ресурсы и оружие на пути из общины. Судя по 
всему, сохранить деньги на получении информации было неправильным выбором: -400 человек, -450 ресурсов, -300 оружия
'''
EVENT_3_3 = '''Возможно пора расширять свои территории. Никакого в округе нет, пограничный патруль сообщил бы вам
об опасностях. Надо лишь помнить, что это займёт много людских сил и ресурсов. Ваш ответ: да/нет
'''
EVENT_3_3_FIRST_YES = '''Было бы о чём волноваться. Стоительные работы прошли успешно. Вы смогли приблизиться к реке,
текущей неподалёку. Доступа к водным ресурсам будет больше. Отличная работа: +30 земли, -20 ресурсов
'''
EVENT_3_3_SECOND_YES = '''Было бы о чём волноваться. Стоительные работы прошли успешно. Вы решили продлить территории к
северу, надеясь расширить имеющуюся пашню. Однако вам потребуется потратить ещё больше ресурсов, чтобы её облагородить.
Сейчас вы ничего с этим не делаете: +40 земли, -20 ресурсов
'''
EVENT_3_3_NO = '''Вы не решились на столь масштабный проект. Сейчас есть куда более важные дела.
'''
RESOURCES = '''Вам необохдимо обратить внимание жителей общины в предстоящей речи на несколько приоритетных аспектов 
развития. Жители терпеливо ждут ваш план. Они будут вам верить и направлять свои силы в указанные области. Что вы 
упомянете? Ваш ответ: да/нет
1) Развитие пашни - оценивается в 60 денег
2) Обслуживание оружия - оценивается в 50 запасов
3) Налаживание торговли - оценивается в 20 запасов и 30 денег
4) Обучение людей - оценивается в 50 денег
5) Ремонт штаба и стены - оценивается в 100 денег и 50 ресурсов
'''
DIRECTIONS = '''Развитие'''
RESOURCE_1 = ['сельского хозяйства: ', 'оружейного дела: ', 'торговли: ', 'образования: ', 'ремонтных работ: ']
VINNER_1 = '''Выиграла первая команда'''
VINNER_2 = '''Выиграла вторая команда'''
VINNER_3 = '''Выиграла третья команда'''
ADD_PROBLEM = '''Ну, эти твари, конечно, мерзкие, но от них знаешь, чего ждать. Обычные люди куда страшнее. На вас
напали и забрали почти все деньги, следите за тем, сколько вы продаете ресурсов'''
LOSER = '''Все проиграли'''
NUMBER = ('Раунд')
CHARITY = 'Вы всем помогли'
FIRST_TEAM = 'Первая команда: '
SECOND_TEAM = 'Вторая команда: '