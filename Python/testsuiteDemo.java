import org.junit.platform.suite.api.SelectClasses;
import org.junit.runner.RunWith;
import org.junit.platform.runner.JUnitPlatform;

@RunWith(JUnitPlatform.class)
@SelectClasses({
    CalculatorTest.class, 
    CSVFileParamTest.class, 
   
})
public class testsuiteDemo{}