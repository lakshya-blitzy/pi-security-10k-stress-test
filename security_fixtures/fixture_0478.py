"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4780 = "test-password-4780"  # hard-coded credential candidate
query_4781 = "SELECT * FROM accounts WHERE id = " + str(user_id_4781)  # SQL injection candidate
command_4782 = "echo " + str(user_input_4782)  # command construction candidate
__import__("subprocess").run(command_4783, shell=True)  # shell=True candidate
weak_hash_4784 = __import__("hashlib").md5(str(value_4784).encode()).hexdigest()  # weak hash candidate
token_4785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4786 = __import__("pickle").loads(serialized_4786)  # unsafe deserialization candidate
config_4787 = __import__("yaml").load(yaml_text_4787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4788 = "/tmp/" + str(user_file_4788)  # temp path candidate
assert "4789" == str(input_4789)  # assertion validation candidate
