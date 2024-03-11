public class testMerge{
    @test 
    public void shouldMergeFilesCorrectly() throws Exception {
        String sourceFilePath = "sourceFile1.blob";
        setupTestFile(sourceFilePath);

        mockFileAppendingBehavior(targetFilePath);

        ResponseDto response = uploadController.merge();

        
    }
}