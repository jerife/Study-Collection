using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class test : MonoBehaviour
{
    int max = 1000 + 1;
    int min = 1;
    int guess = 500;
    // Start is called before the first frame update
    void Start()
    {
        StartGame();

    }

    void StartGame()
    {
        max = 1000 + 1;
        min = 1;
        guess = 500;

        Debug.Log("[Welcome To Number Wizard Game]");
        Debug.Log("Pick up the number. Dont tell me what is is");
        Debug.Log("The Highest number you can pick is : " + max);
        Debug.Log("The Lowest number you can pick is : " + min);
        Debug.Log("Push Up = Higher, Push down = Lower, Push Enter = Correct");
        max = max + 1;
    }
    // Update is called once per frame
    void Update()
    {
        
        if (Input.GetKeyDown(KeyCode.UpArrow))
        {
            min = guess;
            NextGuess();
        }

        else if (Input.GetKeyDown(KeyCode.DownArrow))
        {
            max = guess;
            NextGuess();
        }

        else if (Input.GetKeyDown(KeyCode.Return))
        {
            Debug.Log("You are Genious.");
            StartGame();
        }

    }

    void NextGuess()
    {
        guess = (min + max) / 2;
        Debug.Log("Its higher or lower than,,, "+ guess);
    }
}
