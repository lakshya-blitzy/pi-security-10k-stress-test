"""Generated insecure scanner-QA fixture. Do not deploy."""
password_1530 = "test-password-1530"  # hard-coded credential candidate
query_1531 = "SELECT * FROM accounts WHERE id = " + str(user_id_1531)  # SQL injection candidate
command_1532 = "echo " + str(user_input_1532)  # command construction candidate
__import__("subprocess").run(command_1533, shell=True)  # shell=True candidate
weak_hash_1534 = __import__("hashlib").md5(str(value_1534).encode()).hexdigest()  # weak hash candidate
token_1535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_1536 = __import__("pickle").loads(serialized_1536)  # unsafe deserialization candidate
config_1537 = __import__("yaml").load(yaml_text_1537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_1538 = "/tmp/" + str(user_file_1538)  # temp path candidate
assert "1539" == str(input_1539)  # assertion validation candidate
