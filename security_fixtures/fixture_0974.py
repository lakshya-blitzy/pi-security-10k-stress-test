"""Generated insecure scanner-QA fixture. Do not deploy."""
password_9740 = "test-password-9740"  # hard-coded credential candidate
query_9741 = "SELECT * FROM accounts WHERE id = " + str(user_id_9741)  # SQL injection candidate
command_9742 = "echo " + str(user_input_9742)  # command construction candidate
__import__("subprocess").run(command_9743, shell=True)  # shell=True candidate
weak_hash_9744 = __import__("hashlib").md5(str(value_9744).encode()).hexdigest()  # weak hash candidate
token_9745 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_9746 = __import__("pickle").loads(serialized_9746)  # unsafe deserialization candidate
config_9747 = __import__("yaml").load(yaml_text_9747, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_9748 = "/tmp/" + str(user_file_9748)  # temp path candidate
assert "9749" == str(input_9749)  # assertion validation candidate
