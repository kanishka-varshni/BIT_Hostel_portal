<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BIT Hostel - Login</title>
    <link rel="stylesheet" href="css/styles.css">
    <style>
        /* General Styles */
        body, html {
            height: 100%;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Roboto', sans-serif;
            background-color: #e6ebf5;
            background-image: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%);
        }

        /* Login Container */
        .login-container {
            background-color: #f1f4f8;
            padding: 80px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
            text-align: center;
            max-width: 900px; /* Max width for container */
            width: 100%;
            aspect-ratio: 1; /* Ensures width and height are the same */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }

        /* Logo Style */
        .login-container img.logo {
            max-width: 1000px;
            margin-bottom: 20px;
        }

        /* Heading Style */
        h1 {
            margin-bottom: 20px;
            font-size: 28px;
            color: #333;
            font-family: 'Montserrat', sans-serif;
        }

        /* Label Style */
        label {
            display: block;
            margin-bottom: 10px;
            font-size: 16px;
            color: #333;
        }

        /* Input Style */
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 12px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
            background-color: #f9f9f9;
        }

        /* Button Style */
        button {
            padding: 12px 20px;
            background-color: #007BFF;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-bottom: 15px;
            width: 100%;
        }

        button:hover {
            background-color: #0056b3;
        }

        /* Google Sign-In Button */
        .google-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 10px;
            background-color: #db4437;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
            width: 100%;
            text-decoration: none;
        }

        .google-btn img {
            margin-right: 10px;
            width: 20px;
            height: 20px;
        }

        /* Footer Style */
        .main-footer {
            position: absolute;
            bottom: 10px;
            width: 100%;
            text-align: center;
            color: #aaa;
            font-size: 14px;
        }
    </style>
</head>

<body>
    <div class="login-container">
        <!-- Logo Image -->
        <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEBUTExEWFRMVFRkWFRcWGRcVFxkTFRkaFh4gFxgYHykgGxolGxMZIjIhJSorLjAuFx8zODUsNygtLisBCgoKDg0OGxAQGislHSU3LS0tMCstKzUrLTIrNy0tLS8tLS01LS0tLS0tLS0tLTcrLS4tLTUrKy0tLS0tLS0tLf/AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAgIDAQAAAAAAAAAAAAAABQYEBwEDCAL/xABHEAABAwIDBAcDCgMECwEAAAABAAIDBBEFEiEGEzFBBxQiUWFxgTJUkxYjQlJicoKRobEVJMEzc5LhNUNTdKKys8LS0/E2/8QAGQEBAAMBAQAAAAAAAAAAAAAAAAECAwQF/8QAJxEBAQABBAEDAwUBAAAAAAAAAAECAxESMSEEMkETFFEzQmGR0SL/2gAMAwEAAhEDEQA/AN4oiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIuLrgvHeEH0i+d4O8fmuboOUREBERAREQEREBERAREQEREBERAREQEREBERAXF1H45jMNJCZpn5WDQc3OdyDRzJWmNqekSqq7sjJgh+qw9tw+28fsLDzWulo5anXSLZG0Notu6KkJa6TeSj/VxWc4H7R9lvqbrX2L9K1XIctPGyEE2BI3sn69m/hYqs7K7LT18hbELMafnJHewy+vq7wHrbit17L7F0tEAWMzy85X2L7/AGeTB4D1JXRljpaPfmq+a1jT4LjldZznThh5yyGFnwwQfH2eSzouiKqeby1MQJ1JAfIb+tr+d1uOy5Wd9Vn8bRPGNM1HRBVNuY54XW4XD2G/oDZR9Tg2N0JLgajKPpRSGVnqwEnlxLVvZcJPVZ/u2pxjSuD9KtXGQJ2MnaDYm27k/NvZuPJbE2c27oqwhrZN3Kf9XL2XG/1T7LvIG6bT7D0laCXM3c3KWMAOv9ocHjz17iFpXajZmeglyTC7Xf2cjfYeB3dx72nUfqtMcdLW68VF3j0jdFo7ZDpHnpSI5yZ4NBrrIwcOy4+0PA+hC3LhWJxVMTZYXh8bhoR+xHEOHMHULn1dHLTvnpaXdmIiLJIiIgIiICIiAiIgIiICIiAiIgLHxCsZDE+WR2WNjS5x7gBf1Pgshaq6accI3dG06ECWXxFyGD82l3oFppYc8pii3aKNtftLJX1BkddsbdIo76Mb/wCR4k+Q5BdWyuAvrqpsDNAe1I76kY4nz1AHiR4qIW7Oh7CBFRGcjtzuJ8d2wlrR+eY+q9HVymlp/wDLOeauOEYXFTQthhblY0WA5k8y483HiSs1FWNtJ61sf8s3sW7bm6yj7reQ8Rc+XFeTlltN62k38MnaHamCkFic8ttI2nX8R+iP18FRa9+I1wEu7kMY1YGdlo8Wi93Hx1UPg9VFHUNknjMrASXN5k95v7RB1seK27TYiyohLqWRhNrNuCQ13IPaCCFzTL6vd2/hfbii8FrZ6anz4hMxo+gDrJ5OI9o+ABPeVN4biUVQzPE8Pb4cQe4jiD5qnybNNANRidTmd3BxDR4A2ufutA9VVcJbN1s9Rz+0cpP+zvpvOVrd/wC6n6lw2m3+nGVuZRm0WCxVlO6CUaO1a4cWvHBw8R+vBZVC5+RolLN6AM+S+W/hfW2iyV0y/MZvMOMYbJTTvglFnxuse4jiCPAix9VKbGbUSUE4eLuhcbTR/Wb3jueOI7+HPS+dNGCB0cdW0dphEUnixxu0nydp+NajXr6eU1dPyyvivUlHUsljbJG4OY9oc0jgWnULuWsuhbGS+KSlcf7L5yP7jz2h6P1/Gtmry9TDhlcWku4iIqJEREBERAREQEREBERAREQCvPXSRUF+K1N/ouawa3sGxt4etz6lehVofpZw4xYk99uzOxsg7rgCN3rdl/xLq9HZzVy6U1ekdjow3D6UDh1eL9WA/wBV5uXovYOpEmG0rtNIWsNu+MZD+rVt632xXBPLVNXtBPS10+7fdm+feN2rDqeX0T4hbWWmcekyYhK618s5dbvyuzW/RePr2ySxvhN1kc2hxPh/LVR8rOP7P/RyrtZh9Xh8od2mG/ZkYbtd4X5/dcrNi8VFiEL54niOeNheQbNccovZ45/eH+S+ej/HppZeryu3jMhc0u1cC0jQniRrz1Wdktm/f5i2/hiUuAVFUes10xjiAvd5DXW+y06Mb6enNc1+1sUDDBQRhjechGpPeAdSftO/JRvXJsRrGRTSFrXPIDR7LQAToObtLXPf6KW22oqKngbDE1omDgebn5bG5e7xuND6BRv4tx/v5T8+Wb0Yyuf1h73Fzi5l3ONyTZ3ElXpUTorHYn+839ir2ujR9kZ59oXbSkEuH1LDzheRfk5ozA/m0LzevSW2FSI8PqXngIHjuuS0tA9SQvNq9X0XtrHNceiaYtxSMD6bJGnyy5v3YFvlaR6G6Avr3S/Rhidc/ak7IH5Zj6Ldyw9X+otj0IiLmWEREBERAREQEREBERARFgY3jENJC6aZ2Vjfzc7kGjm49ymTfxBnqp9I2zPXqXsD5+K74vtfWb+IDTxAViwzEI6iJk0Tg6N4u0j8te4gggjkQslTjlcct53Dt5Xc0gkEEEGxB0II0IIPArbHQvjgLJKNx1aTLF4tPtgeRsfxFSfSBsAKsmenysqLdoHRstuFzyfyzc+B5Eahp5p6OpDgDHPC/g4ahw4gjmCDbxBXo8sdfT2nbP216bWqNrsNlgrHTujJidKHtdxadQbO7jcWsVe9kdpoq+ASM0eABLHfVj/6tOtjz87hTUkYcCCAQRYgi4IPeF5Orpb+L3GuOWyg4vhtDWQPqYHtjka0uc3RtyBms9h4E29ofqo/oyH847whd/zMUztDsCx930xDHcd2fYP3T9H9R5KN6PqSSGveyVhY8Qu0I+2zUd48Vz8bNSbxpvONV6mpZJK3dxOyyGV+Q3tYtLje47gCrDtLskynpHTGR8k+dt3HgS92U6cefEknQLo2Tw6V+I71rDu45ZczuA1ztsDzNyNAtnOYDxF9bjnqE09OZY3cyy2qq9HmFSwQvMrCwyOBa0+1lAtqOXkrauFX9sdqoqCHO6zpXXEUd7Fx7z3MHM/1XVp4dYxnb8qp0zY8GxMo2ntyESSeEbT2QfNwv+A961HFGXODWtLnOIDQBcknQADmVmTSz1lSXG8k8z+Wl3HQAX4AaAdwC3HsBsE2jtNNZ9SRpbVsQI1De92pBd6Dx9Tlj6fDa9svdUpsBs31GkDHW3zznlI+seDR4NFh4m55qyrhdFdWMhjdJI4NYxpc5x4ABedbcrve2jIRVzYza2LEI3lgySRus+Mm5DXE5HXtwIafUEeKsajLG43agiIoBERAREQEREBEUVtTjPUqOapLM4hZmLQct9QONtOKCVUDtls4yvpTE42eDnid9WQAgE+BDiD4FV6l6RZGinkqsOlp6epcxsU4kjmbeQXbmaw5mg35hTu3W1TMNpd+6MyuLwxkbTYucQXHWx4Na4+imWy7waajocWps0TGVjAHG4i32QuHNpZob944r6BxnvxD86lbpdtGw4aa9jS5nVjUBt7EgMz5SeR5LC2d21hrMNfXRt/s2SGSIntNfE0uLSbcxYg9zgur7r84xTi1THTY27h1/wDxzD93LEn2VxORxe+lqHvOpc4FzifEk3K2lX9IQiwaPE+rkiQt+az2IzOLfat9nuWZi+28UWE/xKJhliLWODbhp7bgwgnWxaSQR3gpPV2dSJ4tVYRgWLUsolhppmPHcNC3iQ4X7TTbh/XVbg2XxyedobU0ctPKOJLbxO+676Pk78ys3FcZZT0b6p47LIt4RzJtcNB7ySAPNYexG07MRpG1DWGM53MfGTcsew2seGtrH8Sy1Nb6nciZNlgXyWi97a9/PX/4PyWvafpHnkNS6PC5JYaWWSOWRksVwYjqQx1nHQX0upWu27ibSUdVFG6SOsnjhaCQxzDLcXdx1aWkED81ilbmtA0AsFyiqG2O3cWH1NNA+Nz9+4Z3A2EUZe1gc7wu4/4SgktqMYngbampJKiVw0sAI2+L3Ei/DgP0WnsU2axeqldNNSyvkdxJMYsBwDRmsGi50Hee9bh202hGH0MtWYzII8nZBy3zvbHxsfr39FlbPYxHV0kVUzRkrA+x+j3gnwII9Ftpa10+pEWbtGx7C4oCCKOQEagh8QIPgc+iyvkrjf8Asqj47P8A2rZuwe28eKCodHEWMgkDGuJvnabkOtYFtw3ge9c9Hm28eKwySNjMTon5HMJDtCLggjkdR+ErX7vL8RXg1ZLsZi7vappnfeljd+8i6m9H+JkgdTcPN8Nh/wAa2u3bmM4z/C2xkuDMz5M2jXZN5ly217Jbrfn4Lnb7biPC2wl8bpDK43a02LYm2zPOh0GZot4p95l+Inizdi9mmUFMIxZ0jrOlePpP8OeUcB/mVYFFY/jApqOWqDd42KIygA2zAC+h8VGYFtnFV4Y6vjboyN7nx31a+MElpNvDQ24EFcuWVyu9WWhFG7N4r1ukhqQzJvo2yZb3tmF7X5qSUAiIgIiICIiAqn0rf6GrP7n/ALgrYozaalglpJmVN9wY3GWxIO7b2j7OvBvJBqDE6appMOw+tqqoVdHF1d4pHMZCWlzRlLHMtvXMHBr78CTzVi2tr5qnF44oKM1bKKBz5Y942ECWqaWDNn5iO9ha4zLIwjZ7A+tUrGl8sz4G1FKyd80jd0NQWNkOUEAXynXQ6aKSpsZw2ibJVsMrjWzvDi1ksr3ywZ2us0C4YwMf4ADRBTtja6RuB4pQTNLJaJk7MjiHOEUjHuFyNDZ2bUaWtZYkLDh+GwVjB/K1tAIKsAEhlQYi2KWw7ycjj5cSVcK4YR155O+6xiNOGOyMqSyWGRrG3GVuUWGW7tMt9bXKyK3F8KioGUj94aWQPpWARTyXMbzCWZmtJz52kDmSLi6Ch49/+Lp/vM/6z19dKUJw6nq6UA9Tri2ensCWxVLZGulj8GuHaHIWIV2xCjwj+HPoZC8UtLJEx7fnczZJi18YvbMbmZvlfXgsvaCuwzEHSYfUNke6O8jmmKdmXd5u0JMoAHZcAQbO1AvdBDdItZI+PD6GCEzySvjnkiDgzNBTASEFztGguDdT9VYnR3iE0GM1lLUU/VjV/wA5HFnbJZx0fZzNDm1P4FadmZKCrqeuU4mdI2nbC18jJ42bgm43e8aGuuW8Rc/msXautwyPEIZpt66spmEjcMlkMcT73MojBAaQ53HkTZBrCnq6+GDE3wysZRuxKWKqcI95NHHI7K6RutiA02tx19Rc9tMMhpsOwmGndnhZiFLkfcOzA5nZrjQ3Jvppqp6F+FUdM5zbyQYlI95DWy1O+fI0l1msBNsrXXFtLFK7BcOp8Og3gn6rTysqIR8/I9jgC5t2gF4YLk5SLDnZBdVozH21WJHFZYqB08MpFPDMJI2btlG7NdrXdpwdIC7Tjey2ZVba0RijJdNapY8xBkFQXljLNc4NazM0doWJHMELHjxTD8Jhio4xJ7BeyGNkk8u7c4kue1oLg3M46u8uSCn7TY713Y905Pbywsk/vI6iNhPra/4ljYZXyUGHVeHMvvHiDqNzqW4i0N7Pfkk3hv3+is2H4VgslIKSIuNPiUr3tYHS6yw2e4a6xkboXBt7NlmV7MJElLVymzqabqUD3ZwBK0lmV2ljYg9o6c7oIPoXoGU8uKwM9iKq3bb6mzM7f6Kp9EE4odzVONoKvrEExNsolgG+jNzwuwSN9StrYTHh9JPX7t+SS7aisL3Oyt3udwdmd2QNHaDhZVvBaXA6qmbhjGytikcZomzCaIykDMXQvkALhbWw5FBWNioXHH6SpkBEtbTT1Txe9myvlEYHdaJrFJbROqa/EK/c0Jqoo4Dh7HCaOIRyOG8kcA/i4OLR+AK8U1Hh8k38QacrqNklLnJcxkbIS5rwWusLNu7teCwdicbwxh6tSmRhne+ZhmZK3rD3AOc5kkgG80A9LckFbwfGXVOydS15+dp4JaeQH2gYm2bfnfIW+oKjZGHDcPhqWg9UxDDY4qkC5EdX1YCOSwvYP9g+NiVZcSkwakkroCJj1nWu3TZpY482Z13uYC2I2c4m2tuPJTtU/DDSMoJHg0z6LPHfNldSQtaMzZOBc1pa7jm5oO/o1/0RRf7vH+ysqjNmI4G0cAps3V903dZswO7Iu2+btcDzUmgIiICIiAiIgKN2lhdJRVLGNLnvp5WtaOJc5jgAPEkqSXXPFmaW3IuCLtNnC4tcHkfFBqtux1RNLSXjdE+DCYhFMbfNV0UjXBptrwzBwGhBK+YsNqmYRTtmoajrbZqiUPpSzfU075ZHMLWl1nRuDyCLkZTzuFffkyPfKz47k+TI97rPjuQQ8FFWPrcLmnj7cdLO2pc22Vs0jYtNNNS13DTRRU2BVJpKJghdmjxkzvGnZg63LJnOvDI4H1Vt+TI97rPjuT5Mj3us+O5BSdqcJq3VFbAykleK2ppJo5m5NyxkG5D964uBaRujpY30VlqMOlOI1sgjOSSgjjY7k6RrpiWjx7bfzWRFhMDnFrcRqHOBsQKq5B7iBzWR8mh73WfHcgr3RPh0sEAjljro3tija4VL2ugDm3v1docco8wNLL7bLU4fW1j+oTVMdXIyWKSmyOcHCNsZZK17gWgFlw7Udr0U/wDJke+Vnx3J8mR73WfHcgp8GyNS6CgjkEkLjWVNRN1aTK6nbO2Z7WiQdxe1pI7z5q7YzRO/h80LM8jurvjbmOZ73bstFzzce/vXT8mR73WfHcnyZHvdZ8dyCkY7g09sMJhrrQ0LopepPbHMyQthGUuLhp2HX15BS7+sUGIVFSKOeqhq44LGEMfNE+FmTLI1zhcHV2YG1yR4qeZs608KyrOpGlQ46jQjzBXX/BIt5u+v1W8tmydZObKLa5eNtRr4oILH8KqK+XDXugnpQ2SodLupGtkia6MhhL2cC4gXAv7RHisKPZF7qSKlmhklj/ikzpN4c7jTuEwEj3c75mnNxuQVcPkyPe6z47k+TI97rPjuQa+p9j8RkbiUM1nOLaNtPK7RtQykc94zm+jnNytdfS55qxT1FTiM9I3+Hz0raaobPLLPuwAY2uGSEtcc+YutmsBlv3hT/wAmR73WfHcuqpwKONpdJXVTGji51QWgeZKCpx4NUz0OI0HV5YnyVNRPFK8NEMjTUCVrMwdm7YFjdtrE8VnVstTiLqWE4dNS7iphqJZZ93kZuDmywFjjnLiMuawFjfwViGzQ98rPjuXPyZHvdZ8dyCnzNr6KOelhpqhz5KmWeGop2Qyse2ZxflmErhuyC4NLjfQXCzNq9m6iqw+iZUN39SyohM7o+yBG85ZgMtvm8jiD3gBWT5Mj3us+O5PkyPe6z47kE41oAsNAOHkuV0UVPu2NZne/L9J7szjz1ceK70BERAREQEREBERAREQFiYrTGWCWNshjdJG9geOLC5paHDxF7+iy1jYnSb6CWLMW7yN7Mw4jO0tuPK6Cg4PiLYpaSixGlFPUQva2knY29PM4MLLRvHsOc0kFju8c7KxmsqDixhD2CFtK2TLlN7ukLXG+a1+wLaaa96+6zAJKgQsqZ2yRwysmAbGY3vkiN2F7s5Fr6kNaLm3AXByJ8Fca5tWyYt+Z3MkeUODmh+8aQ46tN7g8bgngbEBF4ptRNBNldFGGdahgawuzSuinLYxL2CQxud9g1wFww63Nln4ljEsNdTwuawU9Rna2TXMJ2Nzhh1sMzQ4g/YI4kKOq9jZHmW1YQySrjrGjdNc5ssb2PyueT24/mxYaEaakCy+tshFUhuHnemd5ilY5jJBkDJAd4ZmtyNLQxxtcE6AcQgnMErHzRmR2XK5793lBF4muLWuNyb5gMwtyIX1jmJCmp5JjbsNuASGgvOjRc6C7iB6rLgiaxoa0Wa0BrQOAaBYAegUfilBLLLC5sjGxxP3jmOjLi9wBaO0HgC2a40OoB5IKnsDWtgraihNU2oEjRVxSBzXXc+wnHZ0HzvbDe6TwKycXEgx6DctZnNBNq+4AG9i1OXV3dbxUvj+AvnqKaeOZsT6ZzyCY8+ZsjcrmuOZvYI5d4B5LmqwOV1eysbMwFkD4GsMZOkha8kuDxrmYOQ0uPFBiUu14dh0VW6PtyyNgDG5nATum6vxtmLQ8E8L2GlzZZ+EYnUPkmZJAcrA10Uga+NsoI1blk1a9rh5EEHvUbTbFAYb1F87jaR0scsbd29khlM7SAS7Vr3H0sPFSVDhE26e2oq3zPfHu87WthytsRma1t+2b6u+yLAII3CNqpH1cFNKyMOmgfK4RuzbmWIsDo3OBLXkZyCRbVvDVRe22KvqsMxIxNjMMIlgdnvnc+IZZHN5Nykm2hzFvIEFSWEbHyQy0chqs3VIHU7WtiaxrojktzJDvmxc8DyDVxWbFvcyshjqiynrTI+SMxh7mSyjtmN+YWa46lpB52IQWyD2G+Q/Zdi66dhaxoJuQACbWuQLXtyXYgIiICIiAiIgIiICIiAiIgIiICIiAiIgLhcogIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIg/9k=" alt="BIT Hostel Logo" class="logo"> <!-- Replace with the correct path or URL -->

        <h1>BIT Hostel</h1>
        <form id="loginForm">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <button type="submit">Login</button>
        </form>
        <a href="#" class="google-btn">
            <img src="https://www.gstatic.com/images/branding/product/1x/gsa_512dp.png" alt="Google logo">
            Sign in with Google
        </a>
    </div>

    <footer class="main-footer">
        <p>&copy; 2024 BIT Hostel. All Rights Reserved.</p>
    </footer>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent form submission

            // Get the username and password values
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Redirect based on credentials
            if (username === 'admin' && password === 'admin') {
                window.location.href = 'admin/index.html';
            } else if (username === 'student' && password === 'student') {
                window.location.href = 'student/index.html';
            } else if (username === 'warden' && password === 'warden') {
                window.location.href = 'warden/dashboard.html';
            }else {
                alert('Invalid username or password');
            }
        });
    </script>
</body>

</html>
