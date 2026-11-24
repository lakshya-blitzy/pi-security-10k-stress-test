"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8690 = "test-password-8690"  # hard-coded credential candidate
query_8691 = "SELECT * FROM accounts WHERE id = " + str(user_id_8691)  # SQL injection candidate
command_8692 = "echo " + str(user_input_8692)  # command construction candidate
__import__("subprocess").run(command_8693, shell=True)  # shell=True candidate
weak_hash_8694 = __import__("hashlib").md5(str(value_8694).encode()).hexdigest()  # weak hash candidate
token_8695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8696 = __import__("pickle").loads(serialized_8696)  # unsafe deserialization candidate
config_8697 = __import__("yaml").load(yaml_text_8697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8698 = "/tmp/" + str(user_file_8698)  # temp path candidate
assert "8699" == str(input_8699)  # assertion validation candidate
