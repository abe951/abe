@Test
 public void ReadData() throws IOException
 {
     // Import excel sheet from a webdriver directory which is inside c drive.
     //DataSource is the name of the excel
     File src=new File("C:\\webdriver\\DataSource.xls");
      
     //This step is for loading the file. We have used FileInputStream as
     //we are reading the excel. The path of the file is passed as an argument to FileInputStream
     FileInputStream finput = new FileInputStream(src);
      
     //This step is to load the workbook of the excel which is done by global HSSFWorkbook in which we have
     //passed finput as an argument.
    workbook = new HSSFWorkbook(finput);
      
     //This step is to load the sheet in which data is stored.
     sheet= workbook.getSheetAt(0);
      
     for(int i=1; i&lt;=sheet.getLastRowNum(); i++)
     {
         // Import data for Email.
         cell = sheet.getRow(i).getCell(1);
         cell.setCellType(Cell.CELL_TYPE_STRING);
         driver.findElement(By.id("email")).sendKeys(cell.getStringCellValue());
          
         // Import data for the password.
         cell = sheet.getRow(i).getCell(2);
         cell.setCellType(Cell.CELL_TYPE_STRING);
         driver.findElement(By.id("password")).sendKeys(cell.getStringCellValue());
                 
        }
  }
