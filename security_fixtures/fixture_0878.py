"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8780 = "test-password-8780"  # hard-coded credential candidate
query_8781 = "SELECT * FROM accounts WHERE id = " + str(user_id_8781)  # SQL injection candidate
command_8782 = "echo " + str(user_input_8782)  # command construction candidate
__import__("subprocess").run(command_8783, shell=True)  # shell=True candidate
weak_hash_8784 = __import__("hashlib").md5(str(value_8784).encode()).hexdigest()  # weak hash candidate
token_8785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8786 = __import__("pickle").loads(serialized_8786)  # unsafe deserialization candidate
config_8787 = __import__("yaml").load(yaml_text_8787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8788 = "/tmp/" + str(user_file_8788)  # temp path candidate
assert "8789" == str(input_8789)  # assertion validation candidate
