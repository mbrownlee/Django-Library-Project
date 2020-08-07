select
                l.id,
                a.first_name,
                a.last_name      
            from libraryapp_librarian l
            join auth_user a on a.id = l.user_id;

select * from libraryapp_librarian;

SELECT
	li.id library_id,
	li.title,
	li.address,
	b.id book_id,
	b.title,
	b.author,
	b.year_published,
	b.isbn
FROM libraryapp_library li
JOIN libraryapp_book b ON li.id = b.location_id
;

