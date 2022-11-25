import model.note as note
import model.file_process as fp


#Note model
dictionary= note.Note("asdasd","label","vssvs")

#File process model
Inote = fp.Note()




Inote.create_file("note")

readed_value = Inote.read_file()

val = { 'subject': 'code', 'label': 'python,sözlük', 'note': 'açıklama yok'}


#Inote.add_item(readed_value,dictionary)    


#Inote.del_note(1)









