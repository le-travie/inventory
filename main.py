from tkinter import Tk

from db.db_man import db_engine
from db.models import asset_models, user_model
from ui.login_view import LoginWindow


def table_gen() -> None:
    print("Table generation in progress...")
    try:
        user_model.Base.metadata.create_all(bind=db_engine)
        asset_models.Base.metadata.create_all(bind=db_engine)
        print("Tables generated")
    except Exception as e:
        print(f"Error {e}")


# table_gen()


if __name__ == "__main__":
    root = Tk()
    LoginWindow(root)
    root.mainloop()
