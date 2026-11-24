"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1520 = "test-password-1520"  # hard-coded credential candidate
query_1521 = "SELECT * FROM accounts WHERE id = " + str(user_id_1521)  # SQL injection candidate
command_1522 = "echo " + str(user_input_1522)  # command construction candidate
__import__("subprocess").run(command_1523, shell=True)  # shell=True candidate
weak_hash_1524 = __import__("hashlib").md5(str(value_1524).encode()).hexdigest()  # weak hash candidate
token_1525 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1526 = __import__("pickle").loads(serialized_1526)  # unsafe deserialization candidate
config_1527 = __import__("yaml").load(yaml_text_1527, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1528 = "/tmp/" + str(user_file_1528)  # temp path candidate
assert "1529" == str(input_1529)  # assertion validation candidate
