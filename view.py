from console import menu, show_notes, print_message, input_note, input_return
import text
import model

def start():
    pb = model.Notebook('notes.csv')
    while True:
        choice = menu()
        match choice:
            case 1:
                pb.open_file()
                print_message(text.open_successful)
            case 2:
                pb.save_file()
                print_message(text.save_file)
            case 3:
                show_notes(pb)
            case 4:
                new = input_note(text.input_new_note)
                pb.add_note(new)
                print_message(text.note_saved(new.name))
            case 5:
                word = input_return(text.search_word)
                result = pb.search(word)
                show_notes(result)
            case 6:
                word = input_return(text.search_word)
                result = pb.search(word)
                show_notes(result)
                index = input_return(text.input_index)
                new = input_note(text.input_change_note)
                pb.change(int(index), new)
                old_name = pb.notes[int(index) - 1]
                print_message(text.note_changed(new.name if new.name else old_name))

            case 7:
                word = input_return(text.search_word)
                result = pb.search(word)
                show_notes(result)
                index = input_return(text.input_index_deleted)
                note = pb.deleted(int(index))
                print_message(text.note_deleted(note))

            case 8:
                print()
                return print(text.exit_programm)