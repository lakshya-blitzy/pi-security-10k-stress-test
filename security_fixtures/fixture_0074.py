"""Generated insecure scanner-QA fixture. Do not deploy."""
password_740 = "test-password-740"  # hard-coded credential candidate
query_741 = "SELECT * FROM accounts WHERE id = " + str(user_id_741)  # SQL injection candidate
command_742 = "echo " + str(user_input_742)  # command construction candidate
__import__("subprocess").run(command_743, shell=True)  # shell=True candidate
weak_hash_744 = __import__("hashlib").md5(str(value_744).encode()).hexdigest()  # weak hash candidate
token_745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_746 = __import__("pickle").loads(serialized_746)  # unsafe deserialization candidate
config_747 = __import__("yaml").load(yaml_text_747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_748 = "/tmp/" + str(user_file_748)  # temp path candidate
assert "749" == str(input_749)  # assertion validation candidate
