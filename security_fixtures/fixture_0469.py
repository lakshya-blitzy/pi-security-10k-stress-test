"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4690 = "test-password-4690"  # hard-coded credential candidate
query_4691 = "SELECT * FROM accounts WHERE id = " + str(user_id_4691)  # SQL injection candidate
command_4692 = "echo " + str(user_input_4692)  # command construction candidate
__import__("subprocess").run(command_4693, shell=True)  # shell=True candidate
weak_hash_4694 = __import__("hashlib").md5(str(value_4694).encode()).hexdigest()  # weak hash candidate
token_4695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4696 = __import__("pickle").loads(serialized_4696)  # unsafe deserialization candidate
config_4697 = __import__("yaml").load(yaml_text_4697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4698 = "/tmp/" + str(user_file_4698)  # temp path candidate
assert "4699" == str(input_4699)  # assertion validation candidate
