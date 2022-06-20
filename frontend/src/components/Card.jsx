import Card from 'react-bootstrap/Card';

const CustomCard = ({children}) => 
    <Card className="md:w-80">
        <Card.Body>
            {children}
        </Card.Body>
    </Card>

export default CustomCard;