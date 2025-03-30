namespace BookStore.Models;

public class Book
{
    public int Id { get; set; }
    public string Title { get; set; } = "Untitled";
    public string Author { get; set; } = "Unknown";
    public decimal Price { get; set; } = 0;
}