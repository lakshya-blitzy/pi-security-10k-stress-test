"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4640 = "test-password-4640"  # hard-coded credential candidate
query_4641 = "SELECT * FROM accounts WHERE id = " + str(user_id_4641)  # SQL injection candidate
command_4642 = "echo " + str(user_input_4642)  # command construction candidate
__import__("subprocess").run(command_4643, shell=True)  # shell=True candidate
weak_hash_4644 = __import__("hashlib").md5(str(value_4644).encode()).hexdigest()  # weak hash candidate
token_4645 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4646 = __import__("pickle").loads(serialized_4646)  # unsafe deserialization candidate
config_4647 = __import__("yaml").load(yaml_text_4647, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4648 = "/tmp/" + str(user_file_4648)  # temp path candidate
assert "4649" == str(input_4649)  # assertion validation candidate
