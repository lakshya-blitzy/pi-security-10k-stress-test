"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3780 = "test-password-3780"  # hard-coded credential candidate
query_3781 = "SELECT * FROM accounts WHERE id = " + str(user_id_3781)  # SQL injection candidate
command_3782 = "echo " + str(user_input_3782)  # command construction candidate
__import__("subprocess").run(command_3783, shell=True)  # shell=True candidate
weak_hash_3784 = __import__("hashlib").md5(str(value_3784).encode()).hexdigest()  # weak hash candidate
token_3785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3786 = __import__("pickle").loads(serialized_3786)  # unsafe deserialization candidate
config_3787 = __import__("yaml").load(yaml_text_3787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3788 = "/tmp/" + str(user_file_3788)  # temp path candidate
assert "3789" == str(input_3789)  # assertion validation candidate
