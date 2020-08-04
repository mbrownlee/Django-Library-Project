select
                l.id,
                a.first_name,
                a.last_name      
            from libraryapp_librarian l
            join auth_user a on a.id = l.user_id;

select * from libraryapp_librarian;

