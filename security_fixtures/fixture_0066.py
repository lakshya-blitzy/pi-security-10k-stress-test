"""Generated insecure scanner-QA fixture. Do not deploy."""
password_660 = "test-password-660"  # hard-coded credential candidate
query_661 = "SELECT * FROM accounts WHERE id = " + str(user_id_661)  # SQL injection candidate
command_662 = "echo " + str(user_input_662)  # command construction candidate
__import__("subprocess").run(command_663, shell=True)  # shell=True candidate
weak_hash_664 = __import__("hashlib").md5(str(value_664).encode()).hexdigest()  # weak hash candidate
token_665 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_666 = __import__("pickle").loads(serialized_666)  # unsafe deserialization candidate
config_667 = __import__("yaml").load(yaml_text_667, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_668 = "/tmp/" + str(user_file_668)  # temp path candidate
assert "669" == str(input_669)  # assertion validation candidate
