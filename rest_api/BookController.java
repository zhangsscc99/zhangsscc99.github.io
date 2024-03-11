import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.ResponseEntity;

@RestController
public class BookController {

    private final BookService bookService;

    // Constructor for BookService injection
    public BookController(BookService bookService) {
        this.bookService = bookService;
    }


    @PostMapping("api/books")
    public ResponseEntity<Book> addBook(@ResponseBody Book newBook) {
        Book book = bookService.addBook(newBook);
        return ResponseEntity.ok(book);
    }
}
