"""Generated insecure scanner-QA fixture. Do not deploy."""
password_640 = "test-password-640"  # hard-coded credential candidate
query_641 = "SELECT * FROM accounts WHERE id = " + str(user_id_641)  # SQL injection candidate
command_642 = "echo " + str(user_input_642)  # command construction candidate
__import__("subprocess").run(command_643, shell=True)  # shell=True candidate
weak_hash_644 = __import__("hashlib").md5(str(value_644).encode()).hexdigest()  # weak hash candidate
token_645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_646 = __import__("pickle").loads(serialized_646)  # unsafe deserialization candidate
config_647 = __import__("yaml").load(yaml_text_647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_648 = "/tmp/" + str(user_file_648)  # temp path candidate
assert "649" == str(input_649)  # assertion validation candidate
