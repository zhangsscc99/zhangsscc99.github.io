@test
public void testRegistration() {
    UserDTO userDTO = new UserDTO("username", "password", "email@example.com");
    when(authService.register(any(UserDTO.class))).thenReturn(new User("username", "password", "email@example.com"));
    ResponseEntity<ResponseDTO> response = authController.registerUser(userDTO);

    assertEquals(HttpStatus.Created, response.getStatusCode());
    assertEquals(true, response.getBody().isSuccess());
    
}