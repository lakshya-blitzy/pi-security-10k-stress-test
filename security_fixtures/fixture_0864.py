"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8640 = "test-password-8640"  # hard-coded credential candidate
query_8641 = "SELECT * FROM accounts WHERE id = " + str(user_id_8641)  # SQL injection candidate
command_8642 = "echo " + str(user_input_8642)  # command construction candidate
__import__("subprocess").run(command_8643, shell=True)  # shell=True candidate
weak_hash_8644 = __import__("hashlib").md5(str(value_8644).encode()).hexdigest()  # weak hash candidate
token_8645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8646 = __import__("pickle").loads(serialized_8646)  # unsafe deserialization candidate
config_8647 = __import__("yaml").load(yaml_text_8647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8648 = "/tmp/" + str(user_file_8648)  # temp path candidate
assert "8649" == str(input_8649)  # assertion validation candidate
