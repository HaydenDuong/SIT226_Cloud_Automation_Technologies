using Microsoft.AspNetCore.Mvc;
using RobotWebApp.Models;

namespace RobotWebApp.Controllers;

public class RobotController : Controller
{
    private static List<string> _commands = new() { "LEFT", "RIGHT", "PLACE", "MOVE" };
    private static RobotMap _robotMap = new();

    // GET: /Robot
    public IActionResult Index()
    {
        ViewData["RobotMap"] = _robotMap;
        return View(_commands);
    }

    // GET: /Robot/Commands
    public JsonResult Commands()
    {
        return Json(_commands);
    }

    // POST: /Robot/UpdateMap
    [HttpPost]
    public IActionResult UpdateMap([FromBody] string mapSize)
    {
        if (CheckMapInput(mapSize))
        {
            var parts = mapSize.Split('x');
            if (int.TryParse(parts[0], out int side))
            {
                _robotMap = new RobotMap {
                    MapSize = mapSize,
                    Side = side,
                    Area = side * side
                };
                return Json(new { success = true, message = $"Map updated to {mapSize}" });
            }
        }
        return BadRequest("Invalid map size");
    }

    private bool CheckMapInput(string mapSizedInput)
    {
        string[] mapSized = mapSizedInput.Split('x');

        if (mapSized.Length != 2)
        {
            return false;
        }

        if (int.TryParse(mapSized[0], out int a) && int.TryParse(mapSized[1], out int b))
        {
            //Check if the input mapSized is a square or not
            if (a == b && a >= 2 && a <= 100)
            {
                return true;
            }
        }
    
        return false;
    }
}
