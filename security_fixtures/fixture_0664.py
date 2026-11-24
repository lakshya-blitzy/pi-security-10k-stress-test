"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6640 = "test-password-6640"  # hard-coded credential candidate
query_6641 = "SELECT * FROM accounts WHERE id = " + str(user_id_6641)  # SQL injection candidate
command_6642 = "echo " + str(user_input_6642)  # command construction candidate
__import__("subprocess").run(command_6643, shell=True)  # shell=True candidate
weak_hash_6644 = __import__("hashlib").md5(str(value_6644).encode()).hexdigest()  # weak hash candidate
token_6645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6646 = __import__("pickle").loads(serialized_6646)  # unsafe deserialization candidate
config_6647 = __import__("yaml").load(yaml_text_6647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6648 = "/tmp/" + str(user_file_6648)  # temp path candidate
assert "6649" == str(input_6649)  # assertion validation candidate
