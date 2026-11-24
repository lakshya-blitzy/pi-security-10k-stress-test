"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6780 = "test-password-6780"  # hard-coded credential candidate
query_6781 = "SELECT * FROM accounts WHERE id = " + str(user_id_6781)  # SQL injection candidate
command_6782 = "echo " + str(user_input_6782)  # command construction candidate
__import__("subprocess").run(command_6783, shell=True)  # shell=True candidate
weak_hash_6784 = __import__("hashlib").md5(str(value_6784).encode()).hexdigest()  # weak hash candidate
token_6785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6786 = __import__("pickle").loads(serialized_6786)  # unsafe deserialization candidate
config_6787 = __import__("yaml").load(yaml_text_6787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6788 = "/tmp/" + str(user_file_6788)  # temp path candidate
assert "6789" == str(input_6789)  # assertion validation candidate
