"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6530 = "test-password-6530"  # hard-coded credential candidate
query_6531 = "SELECT * FROM accounts WHERE id = " + str(user_id_6531)  # SQL injection candidate
command_6532 = "echo " + str(user_input_6532)  # command construction candidate
__import__("subprocess").run(command_6533, shell=True)  # shell=True candidate
weak_hash_6534 = __import__("hashlib").md5(str(value_6534).encode()).hexdigest()  # weak hash candidate
token_6535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6536 = __import__("pickle").loads(serialized_6536)  # unsafe deserialization candidate
config_6537 = __import__("yaml").load(yaml_text_6537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6538 = "/tmp/" + str(user_file_6538)  # temp path candidate
assert "6539" == str(input_6539)  # assertion validation candidate
