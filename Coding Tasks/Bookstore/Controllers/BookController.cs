using BookStore.Models;
using Microsoft.AspNetCore.Mvc;

namespace BookStore.Controllers;

public class BookController : Controller
{
    private static List<Book> _books = new()
    {
        new Book { Id = 1, Title = "The Hobbit", Author = "J.R.R. Tolkien", Price = 10.99m },
        new Book { Id = 2, Title = "Harry Potter", Author = "J.K. Rowling", Price = 12.50m }
    };

    // GET: /Book
    public IActionResult Index()
    {
        return View(_books); // Hiển thị danh sách sách
    }

    // GET: /Book/Add
    public IActionResult Add()
    {
        return View(); // Form thêm sách
    }

    // POST: /Book/Add
    [HttpPost]
    public IActionResult Add(Book newBook)
    {
        if (ModelState.IsValid)
        {
            newBook.Id = _books.Count + 1;
            _books.Add(newBook);
            return RedirectToAction("Index");
        }
        return View(newBook);
    }
}