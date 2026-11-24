"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1510 = "test-password-1510"  # hard-coded credential candidate
query_1511 = "SELECT * FROM accounts WHERE id = " + str(user_id_1511)  # SQL injection candidate
command_1512 = "echo " + str(user_input_1512)  # command construction candidate
__import__("subprocess").run(command_1513, shell=True)  # shell=True candidate
weak_hash_1514 = __import__("hashlib").md5(str(value_1514).encode()).hexdigest()  # weak hash candidate
token_1515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1516 = __import__("pickle").loads(serialized_1516)  # unsafe deserialization candidate
config_1517 = __import__("yaml").load(yaml_text_1517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1518 = "/tmp/" + str(user_file_1518)  # temp path candidate
assert "1519" == str(input_1519)  # assertion validation candidate
