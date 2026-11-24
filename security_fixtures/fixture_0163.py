"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1630 = "test-password-1630"  # hard-coded credential candidate
query_1631 = "SELECT * FROM accounts WHERE id = " + str(user_id_1631)  # SQL injection candidate
command_1632 = "echo " + str(user_input_1632)  # command construction candidate
__import__("subprocess").run(command_1633, shell=True)  # shell=True candidate
weak_hash_1634 = __import__("hashlib").md5(str(value_1634).encode()).hexdigest()  # weak hash candidate
token_1635 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1636 = __import__("pickle").loads(serialized_1636)  # unsafe deserialization candidate
config_1637 = __import__("yaml").load(yaml_text_1637, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1638 = "/tmp/" + str(user_file_1638)  # temp path candidate
assert "1639" == str(input_1639)  # assertion validation candidate
