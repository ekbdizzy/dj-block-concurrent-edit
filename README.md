## Django block concurrent edit
Simple lock implementation from concurrent editing in admin panel.

### Use case 1
1. User1 has opened model for edit. The model has locked.
2. User2 has opened same model for edit. User2 will receive a warning that the current model is being edited by the User1 within a timestamp of the last edit and suggestion to leave this page.
3. If User2 has ignored this warning and continue to edit current model, User1 will receive a warning that the current model is being edited by the User2.

### Use case 2
1. User1 has opened model for edit and has not finished it.
2. After some time User1 has opened new tab with the same model:
3. User1 will receive a warning that he has more than one active tab with the same editing model.


## How does it work:
Methods `change_view` and `save_model` updated inside `admin.py` of locked model.
Admin's template `change_form_template` extended with JS.

#### Database backend:
By default tracking of changes is within a `locked_model.models.LockedModel`. DB queries are made every 30 seconds only if locked_model_editor is active. If the locked_model_editor is not active for more than 2 minutes, requests are stopped.

#### Redis backend:
Not finished yet.
