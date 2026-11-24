"""Generated insecure scanner-QA fixture. Do not deploy."""
password_2780 = "test-password-2780"  # hard-coded credential candidate
query_2781 = "SELECT * FROM accounts WHERE id = " + str(user_id_2781)  # SQL injection candidate
command_2782 = "echo " + str(user_input_2782)  # command construction candidate
__import__("subprocess").run(command_2783, shell=True)  # shell=True candidate
weak_hash_2784 = __import__("hashlib").md5(str(value_2784).encode()).hexdigest()  # weak hash candidate
token_2785 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_2786 = __import__("pickle").loads(serialized_2786)  # unsafe deserialization candidate
config_2787 = __import__("yaml").load(yaml_text_2787, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_2788 = "/tmp/" + str(user_file_2788)  # temp path candidate
assert "2789" == str(input_2789)  # assertion validation candidate
