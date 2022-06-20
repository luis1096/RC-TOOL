import { useState, useRef, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Image from 'react-bootstrap/Image';
import Row from 'react-bootstrap/Row';

import './App.scss';
import Card from './components/Card';
import Navbar from './components/Navbar';
import {checkTemperature, postTestTemp, postTestExtrude, getTestTemp} from './utils/backend';


const App = () => {
    // boolean for when printer is busy
    const [ isBusy, setIsBusy ] = useState(false);
    const [ isBusyE, setIsBusyE ] = useState(false);

    // id for clearing setInterval
    const [ isChecking, setIsChecking ] = useState(null)

    // keep track of extrusion rate and temperature
    const extruderRateRef = useRef(0);
    const tempRef = useRef(0)
    const printerLogRef = useRef("")

    const [ MIN_TEMP, MAX_TEMP ] = [ 0, 500 ]
    const [ MIN_RATE, MAX_RATE ] = [ 0, 500 ]

    // while printer is busy 
    useEffect(() => {
        const requestTemperature = async() => {
            if (isBusy === true) {
                // check every 5 seconds
                await setIsChecking(setInterval(checkTemperature, 5000))
            }
        }

        requestTemperature()

    }, [isBusy])

    useEffect(() => {
        const stopChecking = async() => {
            if (isBusy === false && isChecking !== null) {
                // if printer is not busy stop setChecking
                await clearInterval(isChecking)
            }
        }

        stopChecking()
    }, [isBusy, isChecking])

    const increaseTemperature = e => {
        e.preventDefault()

        const currentTemp = tempRef.current.value

        if (currentTemp < MAX_TEMP) {
            tempRef.current.value++
        }
    }

    const decreaseTemperature = e => {
        e.preventDefault()

        const currentTemp = tempRef.current.value

        if (currentTemp > MIN_TEMP) {
            tempRef.current.value--
        }
    }

    const increaseExtruder = e => {
        e.preventDefault()

        const currentRate = extruderRateRef.current.value

        if (currentRate < MAX_RATE) {
            extruderRateRef.current.value++
        }
        
    }

    const decreaseExtruder = e => {
        e.preventDefault()

        const currentRate = extruderRateRef.current.value

        if (currentRate > MIN_RATE) {
            extruderRateRef.current.value--
        }
    }

    const sendTemp = e => {

        e.preventDefault()
        e.target.disabled = true

        setIsBusy(true)
        postTestTemp(printerLogRef.current, tempRef.current.value)
    }

    const sendExtrude = e => {
        
        e.preventDefault()
        e.target.disabled = true

        setIsBusyE(true)
        postTestExtrude(printerLogRef.current, extruderRateRef.current.value)
    }

    const getTemp = e => { 
        e.preventDefault()
        getTestTemp(printerLogRef.current)
    }

    const cancelPrinter = e => { 
        e.preventDefault()

        setIsBusy(false) && setIsBusyE(false)
         
    }

  return (
    <div className="bg-hero-drill bg-cover bg-no-repeat h-screen overflow-y-hidden">
        <Navbar />
        <Container className="mt-2">
            <Row lg={2} md={1}>
                <Col>
                    <Card className="temp-card">
                        <Form>
                            <Form.Group>
                                <Form.Label className="text-2xl">Temperature</Form.Label>
                                <Form.Control placeholder='°Celsius' type="number" min={MIN_TEMP} max={MAX_TEMP} ref={tempRef} />
                            </Form.Group>
                            <Form.Group className='temp-btn'>
                                <Button type="number" onClick={increaseTemperature} variant="success">+</Button>
                                <Button type="number" onClick={decreaseTemperature} variant="danger">-</Button>
                            </Form.Group>
                        </Form>
                    </Card>
                </Col>
                <Col>
                    <Card className="extrude-card">
                        <Form>
                            <Form.Group>
                                <Form.Label className="text-2xl">Extrusion</Form.Label>
                                <Form.Control placeholder='Millimeters' type="number" min={MIN_RATE} max={MAX_RATE} ref={extruderRateRef} />
                            </Form.Group>
                            <Form.Group className='extruder-btn'>
                                <Button type="number" onClick={increaseExtruder} variant="success">+</Button>
                                <Button type="number" onClick={decreaseExtruder} variant="danger">-</Button>
                            </Form.Group>
                        </Form>
                    </Card>
                </Col>
            </Row>

            <Row> 
                {
                    !isBusy  &&
                    <Col>
                        <Image style={{width: '19rem', marginTop: '6rem'}} src="images/lightbulb.svg" className="ready object-scale-down h-48 w-48" alt="lightbulb"  />
                    </Col>
                }
                    <Col>
                        <Card className="data-card">
                            <textarea onClick={getTemp} placeholder="Waiting For 3D-Printer Data..." ref={printerLogRef} className="resize-none pb-64 border border-solid border-gray-300 px-3 rounded"/>
                            <Form>
                                <Container>
                                    <Row md={2} sm={1}>
                                        <Col className={ !isBusyE ? "cursor-not-allowed" : "cursor-pointer" }>
                                            <Button onClick={sendTemp} variant= {!isBusy ? "success": "secondary"}  disabled={isBusy}>Send Temp</Button> 
                                        </Col>
                                        <Col>
                                            <Button onClick={() => printerLogRef.current.value = ""} variant="primary">Clear</Button>   
                                        </Col>
                                        <Col className={ !isBusyE ? "cursor-not-allowed" : "cursor-pointer" }>
                                            <Button onClick={sendExtrude} variant= {isBusyE || !isBusy ? "secondary": "success"} disabled={!isBusy}>Send Extrusion</Button> 
                                        </Col>
                                        <Col>
                                            <Button onClick={cancelPrinter} variant="danger">Cancel</Button>              
                                        </Col>
                                    </Row>
                                </Container>
                            </Form>
                        </Card>
                    </Col>
            </Row>

        </Container>
    </div>
  );
}

export default App;
