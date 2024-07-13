# AsiaYo Pretest
## API Implementation Assessment

I implemented API tests using Python with the Flask framework, also using SOLID principles and design patterns. Belows are descriptions of how I applied SOLID principles and design patterns in my implementation. 

**SOLID**

- Single Responsibility Principle: Each class or function has a single responsibility.
- Open/Closed Principle: In my code, to add different types of order validation or transformation methods, I can extend the `validate_order` and `format_check_and_transform` functions without modifying the `create_order` function itself. This matches the principle of allowing extension without modification of existing code.
- Liskov Substitution Principle: There are no complex inheritance relationships in the program.
- Interface Segregation Principle: Interfaces were not used in this implementation.
- Dependency Inversion Principle: Both `validate_order` and `format_check_and_transform` functions operate independently of the specific `Order class` implementation. They depend only on the structure and content of the order data, adhering to the principle where high-level modules do not depend on low-level details.

**Design Patterns**

- Strategy Pattern: Encapsulated validation logic in `validate_order` and `format_check_and_transform`, allowing for easy addition or removal of validation conditions without impacting the response functions.
- Facade Pattern: Encapsulated order format checking and transformation functionalities, providing both API endpoints and an HTML interface.

Postman Test Results Example
- 200
![Untitled](AsiaYo%20Pretest%209962a63911a0419d93e27c4dd6466c0c/Untitled%206.png)

- 400
![Untitled](AsiaYo%20Pretest%209962a63911a0419d93e27c4dd6466c0c/Untitled%207.png)

**Unit Testing**

I used pytest for unit testing. Test cases include:

1. Test when the price exceeds 2000.
2. Test when the name contains non-English characters.
3. Test when each word in the name is not capitalized.
4. Test when currency is TWD, expecting a successful response.
5. Test when currency is not USD or TWD.
6. Test when currency is USD and the price exceeds 2000 after conversion.
7. Test when currency is USD and verify the converted price.
8. Test when required fields are missing in the input.
9. Test when input field values have incorrect data types.

The actual pytest results are as follows: 
![Untitled](AsiaYo%20Pretest%209962a63911a0419d93e27c4dd6466c0c/Untitled%208.png)

**Docker**

You can pull the pre-built Docker image from Docker Hub:
```docker
docker pull fangyu070899/asiayo-pretest
```

Alternatively, you can build the Docker image locally using the Dockerfile:
```docker
docker build -t fangyu070899/asiayo-pretest .
```

After obtaining the image, run it locally:
```docker
docker run -p 5000:5000 --rm --name test fangyu070899/asiayo-pretest
```

You can access the HTML interface at http://localhost:5000, where you can directly use templates or modify JSON to test the API. The API endpoint is located at http://localhost:5000/api/orders.

![Untitled](AsiaYo%20Pretest%209962a63911a0419d93e27c4dd6466c0c/Untitled%209.png)