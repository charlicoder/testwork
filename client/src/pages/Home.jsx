import React, { useEffect } from 'react'
import useAuth from '../hooks/useAuth'
import useUser from '../hooks/useUser';

export default function Home() {
    const { user } = useAuth();
    const getUser = useUser()

    useEffect(() => {
        getUser()
    }, [])

    return (
        <div className='container mt-3'>
            <h2>
                <div className='row'>
                    <div className="mb-12">
                        {user?.email 
                            ? <>
                                <div>List user Ethereum balance</div>
                                <div className='m-5'>
                                    <p>Ethereum Balance: {user?.balance !== undefined ? user.balance : 'Balance not available'}</p>
                                </div>
                            </>
                            : 'Please login first'
                        }
                    </div>
                </div>
            </h2>
        </div>
    )
}
