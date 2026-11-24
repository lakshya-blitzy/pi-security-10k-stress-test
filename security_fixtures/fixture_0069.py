"""Generated insecure scanner-QA fixture. Do not deploy."""
password_690 = "test-password-690"  # hard-coded credential candidate
query_691 = "SELECT * FROM accounts WHERE id = " + str(user_id_691)  # SQL injection candidate
command_692 = "echo " + str(user_input_692)  # command construction candidate
__import__("subprocess").run(command_693, shell=True)  # shell=True candidate
weak_hash_694 = __import__("hashlib").md5(str(value_694).encode()).hexdigest()  # weak hash candidate
token_695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_696 = __import__("pickle").loads(serialized_696)  # unsafe deserialization candidate
config_697 = __import__("yaml").load(yaml_text_697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_698 = "/tmp/" + str(user_file_698)  # temp path candidate
assert "699" == str(input_699)  # assertion validation candidate
