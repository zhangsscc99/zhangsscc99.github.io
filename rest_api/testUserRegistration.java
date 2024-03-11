@test
public void testRegistration() {
    UserDTO userDTO = new UserDTO("username", "password", "email@example.com");
    when(authService.register(any(UserDTO.class))).thenReturn(new User("username", "password", "email@example.com"));
    ResponseEntity<ResponseDTO> response = authController.registerUser(userDTO);

    assertEquals(HttpStatus.Created, response.getStatusCode());
    assertEquals(true, response.getBody().isSuccess());

}

//code描述状态。data返回数据。message状态描述。
//对所有接口的返回结构保持统一。
//降低前后端沟通成本。
//后端维护通用的接口服务。
//https://好课推荐。www.bilibili.com/video/BV1AM411L7db/?spm_id_from=333.337.search-card.all.click&vd_source=d4b859b0532ebb11fd37c3b6f643100f